#!/usr/bin/env python3
"""Build the zero-tracker, book-style Sovereign AI Mastery reader.

Markdown is canonical; static HTML, CSS and JS are the publication output.
Solutions are deliberately not copied to dist/.
"""
from pathlib import Path
import re, html, subprocess, shutil, os
from urllib.parse import urlsplit, urlunsplit
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
MOD = ROOT / 'chapters/05-laws-regulation-jurisdiction.md'
PART_NAMES = [
    ('I', 'Foundations', '01–03'), ('II', 'Governance & policy', '04–06'),
    ('III', 'Infrastructure', '07–10'), ('IV', 'Models & agents', '11–14'),
    ('V', 'Security & operations', '15–18'), ('VI', 'Product & business', '19–21'),
    ('VII', 'Platform capstone', '22–24'),
]

def modules():
    data = (ROOT/'TOC.md').read_text(encoding='utf-8')
    found = re.findall(r'^### Module\s+(\d{2})\s+—\s+(.+?)(?:\s+\(Week \d+\))?\s*$', data, re.M)
    assert len(found) == 24, f'Expected 24 modules, found {len(found)}'
    return [(int(n), title) for n,title in found]

def render_md(path):
    if shutil.which('pandoc'):
        p=subprocess.run(['pandoc','--from=markdown+footnotes+pipe_tables+fenced_code_blocks+auto_identifiers','--to=html5','--wrap=none'], input=path.read_text(encoding='utf-8'), capture_output=True, text=True, check=True)
        return p.stdout
    import mistune
    return mistune.create_markdown(plugins=['footnotes','table','strikethrough','url'])(path.read_text(encoding='utf-8'))

def article_content(path,dest,diagram=False):
    soup=BeautifulSoup(render_md(path),'html.parser')
    routing={
      'TOC.md':'curriculum.html',
      'STYLE_GUIDE.md':'editorial.html',
      'CHAPTER_TEMPLATE.md':'CHAPTER_TEMPLATE.html',
      'taxonomy/ONTOLOGY.md':'taxonomy/ONTOLOGY.html',
      'chapters/05-laws-regulation-jurisdiction.md':'modules/05-laws-regulation-jurisdiction.html',
      'chapters/01-sovereign-ai-fundamentals.md':'modules/01-sovereign-ai-fundamentals.html',
      'labs/module-01/README.md':'labs/module-01/index.html',
      'social/module-01/POST.md':'social/module-01/POST.html',
      'labs/module-05/README.md':'labs/module-05/index.html',
      'social/module-05/SLIDES.md':'social/module-05/SLIDES.html',
      'social/module-05/POST.md':'social/module-05/POST.html',
    }
    outdir=(DIST/dest).parent
    for a in soup.select('a[href]'):
        href=a['href'];parts=urlsplit(href)
        if parts.scheme or parts.netloc or not parts.path:continue
        raw=parts.path
        target=(path.parent/raw).resolve()
        try: canonical=target.relative_to(ROOT).as_posix()
        except ValueError: continue
        if not (ROOT/canonical).exists() and canonical not in routing:
            # Older authoring links sometimes use ../labs or ../social even
            # from files already within that same folder.
            fallback=re.search(r'(?:labs|social|taxonomy|diagrams)/[^?#]+',raw)
            if fallback:canonical=fallback.group(0)
        target_route=routing.get(canonical,canonical)
        if target_route.endswith('.md'):
            target_route=target_route[:-3]+'.html'
        # Some relative links name the source readme or docs directly.
        if target_route=='labs/module-05/index.html' and not (ROOT/'labs/module-05/index.html').exists():pass
        relative=os.path.relpath(DIST/target_route,outdir).replace(os.sep,'/')
        a['href']=urlunsplit(parts._replace(path=relative))
    # Pre-render course-authored Mermaid flowcharts as accessible SVG.
    # The Markdown remains the canonical editable Mermaid source.
    source_key=path.relative_to(ROOT).as_posix()
    diagram_assets={
      'chapters/01-sovereign-ai-fundamentals.md': ('diagrams/module-01-claim-chain.svg','Sovereignty claim evidence chain'),
      'taxonomy/ONTOLOGY.md': ('diagrams/sovereignty-ontology.svg','Enterprise sovereignty ontology showing relationships between claims, controls and evidence'),
      'chapters/05-laws-regulation-jurisdiction.md': ('diagrams/module-05-control-graph.svg','Legal control and evidence graph')
    }
    for pre in list(soup.find_all('pre')):
        code=pre.find('code')
        classes=set(pre.get('class') or []) | set(code.get('class') or []) if code else set(pre.get('class') or [])
        if 'mermaid' not in classes and 'language-mermaid' not in classes:
            continue
        if source_key not in diagram_assets:
            if source_key.startswith('chapters/') or source_key.startswith('taxonomy/'):
                raise RuntimeError('Missing website SVG for Mermaid diagram in '+source_key)
            continue  # Template documentation displays authoring syntax.
        asset,alt=diagram_assets[source_key]
        if not (ROOT/asset).exists():
            raise FileNotFoundError('Missing pre-rendered diagram: '+asset)
        figure=soup.new_tag('figure',attrs={'class':'diagram diagram-rendered'})
        img=soup.new_tag('img',src=os.path.relpath(DIST/asset,outdir).replace(os.sep,'/'),alt=alt,loading='lazy')
        figure.append(img)
        caption=soup.new_tag('figcaption')
        caption.string='Source-authored Mermaid flowchart, pre-rendered to SVG for reliable reading. Expand below to inspect the original definition.'
        figure.append(caption)
        details=soup.new_tag('details',attrs={'class':'diagram-source'})
        summary=soup.new_tag('summary')
        summary.string='View Mermaid source'
        details.append(summary)
        example=soup.new_tag('pre')
        source=soup.new_tag('code')
        source['class']='language-mermaid'
        source.string=pre.get_text()
        example.append(source)
        details.append(example)
        figure.append(details)
        pre.replace_with(figure)
    sections=[(h.get('id'),h.get_text(' ',strip=True)) for h in soup.find_all('h2') if h.get('id')]
    return str(soup),sections

def relroute(num):
    return 'modules/01-sovereign-ai-fundamentals.html' if num==1 else ('modules/05-laws-regulation-jurisdiction.html' if num==5 else f'curriculum.html#module-{num:02}')

def book_sidebar(page,prefix=''):
    links=[('index','Opening pages','index.html'),('curriculum','Complete contents','curriculum.html'),('ontology','Taxonomy & ontology','taxonomy/ONTOLOGY.html'),('studio','Decision studio','onboarding/index.html')]
    core=''.join(f'<a class="toc-special {"is-active" if page==name else ""}" href="{prefix}{route}">{html.escape(label)}</a>' for name,label,route in links)
    parts=[]; seq=modules(); j=0
    for roman,title,range_text in PART_NAMES:
        lo,hi=[int(x) for x in range_text.split('–')]
        items=[]
        for n,t in seq:
            if lo <= n <= hi:
                active=(page=='module01' and n==1) or (page=='module' and n==5)
                items.append(f'<a class="toc-chapter {"is-active" if active else ""}" href="{prefix}{relroute(n)}" title="{html.escape(t,quote=True)}"><span class="chapter-num">{n:02}</span><span class="chapter-text">{html.escape(t)}</span>{"<span class=\"read-dot\" title=\"Chapter ready\"></span>" if n in (1,5) else ""}</a>')
        opened= ' open' if ((page=='module' and lo<=5<=hi) or (page=='module01' and lo<=1<=hi)) else ''
        parts.append(f'<details class="toc-part"{opened}><summary><span class="roman">{roman}</span><span>{html.escape(title)}</span><span class="chevron">⌄</span></summary><div class="toc-chapters">{"".join(items)}</div></details>')
    return f'''<aside class="book-sidebar" id="book-sidebar" aria-label="Book table of contents">
      <div class="book-logo"><span class="logo-glyph">S<span>/</span>A</span><span class="logo-copy">THE SOVEREIGN AI<br><strong>FIELD GUIDE</strong></span></div>
      <div class="sidebar-label"><span>YOUR READING DESK</span><span>{"05" if page=="module" else "01"} / 24</span></div>
      <nav class="toc-nav" aria-label="Course contents"><div class="toc-top">{core}</div><div class="toc-heading">TABLE OF CONTENTS <span>24 CHAPTERS</span></div>{''.join(parts)}</nav>
      <div class="sidebar-bottom"><span class="bottom-icon">✦</span><span>Written for the thoughtful<br><strong>AI product leader.</strong></span></div>
    </aside>'''

def topbar(page,prefix=''):
    return f'''<div class="reader-topbar"><button class="mobile-menu" type="button" aria-label="Open table of contents" aria-expanded="false">☰ <span>Contents</span></button><a class="mobile-brand" href="{prefix}index.html">S/A <span>FIELD GUIDE</span></a><span class="edition-label">A READER'S EDITION <span class="tiny-sep">/</span> 2026</span><div class="top-actions"><a href="{prefix}onboarding/index.html">Decision studio <span>↗</span></a><a href="{prefix}taxonomy/ONTOLOGY.html">Ontology <span>↗</span></a><button type="button" id="notes-toggle" aria-controls="reader-notes" aria-expanded="true">✎ <span>My notes</span><span class="notes-count" id="notes-count">0</span></button></div></div>'''

def notes_panel():
    return '''<aside class="notes-rail" id="reader-notes" aria-label="Personal annotations"><div class="notes-header"><div class="section-number">THE MARGIN</div><h2>Your field notes <span>✎</span></h2><p>Highlight a sentence in the text. Save a thought beside it.</p></div>
      <div class="notes-toolbar"><button id="show-all-notes" type="button" class="text-action">All notes</button><span id="sync-status" aria-live="polite">Local draft</span></div>
      <div id="notes-list" class="notes-list"><div class="empty-notes"><span>“</span><p>Good reading leaves traces.<br>Select a passage to begin.</p></div></div>
      <div class="sync-card"><div class="sync-top"><span class="sync-mark">↗</span><strong>Sync with GitHub</strong></div><p>This is a <b>public learning journal</b>. GitHub-sync makes your highlights and notes visible to everyone. Never write secrets or customer data.</p><details id="sync-details"><summary>Connect for sync</summary><label for="notes-repo">Public notes repository</label><input id="notes-repo" type="text" value="shantanuchandra/sovereign-ai-mastery" autocomplete="off" spellcheck="false"><label for="github-token">Fine-grained GitHub token</label><input id="github-token" type="password" autocomplete="off" spellcheck="false" placeholder="github_pat_…"><p class="token-help">Scope: this repository only; Contents: read & write. Token is held in memory, never written to local storage or the repository.</p><button type="button" id="connect-github" class="sync-button">Connect & sync</button><button type="button" id="disconnect-github" class="text-action" hidden>Disconnect</button></details><button id="sync-now" class="text-action" type="button">Load shared notes from GitHub ↗</button></div>
      <div class="rail-end">ANNOTATIONS / V1 <span>•</span> MARKUP AS MEMORY</div></aside>'''

def frame(body,page,title,prefix='',article=False,toc=None):
    if article:
        toc_lines=''.join(f'<a href="#{html.escape(k,quote=True)}">{html.escape(v)}</a>' for k,v in (toc or []))
        body=f'''<div class="read-content-header"><div class="book-eyebrow">THE LIBRARY <span>/</span> {html.escape(title)}</div><div class="reading-tools"><span class="chapter-status">CHAPTER IN PROGRESS</span><span class="reading-time">READ / ANNOTATE / REVISIT</span></div></div><div class="prose" data-annotatable="true" data-page-id="{html.escape(page)}">{body}</div><nav class="on-page"><div class="section-number">IN THIS CHAPTER</div>{toc_lines}</nav>'''
        if page=='module01' and title=='Module 01':
            body+='''<section class="chapter-next"><div class="section-number">AFTER THIS CHAPTER</div><h2>Test the sovereignty claim.</h2><p>Build a claim register, run its local structural checks and review the question-led carousel.</p><a class="simple-link" href="../labs/module-01/index.html">Open practical lab ↗</a><a class="simple-link" href="../onboarding/index.html">Try Decision Studio ↗</a><a class="simple-link" href="../social/module-01/CAROUSEL.html">Open question deck ↗</a></section>'''
        if page=='module' and title=='Module 05':
            body+='''<section class="chapter-next"><div class="section-number">AFTER THIS CHAPTER</div><h2>Turn the question into a decision.</h2><p>Try the local lab, then explore the HTML version of the LinkedIn question deck.</p><a class="simple-link" href="../labs/module-05/index.html">Open practical lab ↗</a><a class="simple-link" href="../social/module-05/CAROUSEL.html">Open question deck ↗</a></section>'''
    outer=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{html.escape(title)} — Sovereign AI Field Guide</title><meta name="description" content="A sourced, annotated book on enterprise sovereign AI product leadership."><link rel="stylesheet" href="{prefix}assets/site.css"></head>
    <body data-repo="shantanuchandra/sovereign-ai-mastery" data-page="{html.escape(page)}"><a class="skip-link" href="#main">Skip to chapter</a><div class="reading-layout">{book_sidebar(page,prefix)}<div class="reading-main">{topbar(page,prefix)}<div class="reading-grid"><main class="book-page" id="main">{body}<div class="page-bottom"><span>THE SOVEREIGN AI FIELD GUIDE</span><span>◆</span><span>LEARN • BUILD • QUESTION</span></div></main>{notes_panel()}</div></div></div>
    <div class="selection-toolbar" id="selection-toolbar" hidden role="toolbar" aria-label="Selection options"><button type="button" id="add-highlight">Highlight</button><button type="button" id="add-note">✎ Add note</button></div>
    <dialog id="note-dialog"><form method="dialog" id="note-form"><div class="dialog-eyebrow">FIELD NOTE / YOUR READER'S MARGIN</div><h2>What are you thinking?</h2><blockquote id="selected-quote"></blockquote><label for="note-body">Your note</label><textarea id="note-body" rows="5" maxlength="2000" placeholder="Question an assumption, note a decision, or connect this to your work…"></textarea><div class="dialog-actions"><button type="button" id="cancel-note">Cancel</button><button type="submit" id="save-note">Save note</button></div></form></dialog>
    <script defer src="{prefix}assets/site.js"></script><script defer src="{prefix}assets/annotations.js"></script></body></html>'''
    return outer

def write(path,s):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(s,encoding='utf-8')

def home():
    return '''<div class="home-cover" data-annotatable="true" data-page-id="index">
      <div class="book-eyebrow">VOLUME I <span>——</span> AN EXECUTIVE FIELD GUIDE</div>
      <div class="cover-ornament" aria-hidden="true"><span>✳</span><i></i><span>✳</span></div>
      <div class="cover-title"><span class="cover-pretitle">THE QUESTION THAT STARTS EVERYTHING</span><h1>Who controls<br>the <em>intelligence?</em></h1><p class="cover-deck">A working book about sovereign AI: the architecture, the power structures, and the decisions behind enterprise autonomy.</p></div>
      <div class="cover-rule"></div>
      <div class="cover-meta"><div><span>THE COURSE</span><strong>24 chapters<br>7 parts</strong></div><div><span>THE PRACTICE</span><strong>Technical labs<br>Product decisions</strong></div><div><span>THE FOCUS</span><strong>UAE & GCC<br>Global perspective</strong></div></div>
      <div class="opening-note"><span class="section-number">EDITOR'S NOTE / 001</span><p>Most discussions about sovereign AI begin with a map. <strong>Where is the data?</strong> That is only one of several necessary questions. The harder questions concern who can change a model, who can operate the infrastructure, whose laws apply, and what happens when a vendor relationship ends.</p><p>This field guide is built for product leaders who must answer those questions in architecture reviews, boardrooms, and actual deployments. Not by borrowing certainty from a vendor brochure, but by tracing each claim to a control and to evidence.</p><a class="reading-link" href="modules/01-sovereign-ai-fundamentals.html">Begin with Module 01 <span>↗</span></a></div>
    </div>
    <div class="reading-section" data-annotatable="true" data-page-id="index-section">
      <div class="section-intro"><span class="section-number">01 / THE FRAMEWORK</span><h2>Four questions before one architecture.</h2><p>Sovereignty is not a binary product label. Start with four dimensions of control and make every claim testable.</p></div>
      <div class="dimension-grid"><a href="taxonomy/ONTOLOGY.html"><span>01</span><strong>Territorial</strong><p>Where are data, compute, backups, and logs actually located?</p><b>↗</b></a><a href="taxonomy/ONTOLOGY.html"><span>02</span><strong>Operational</strong><p>Who has administrative access, key custody, and shutdown authority?</p><b>↗</b></a><a href="taxonomy/ONTOLOGY.html"><span>03</span><strong>Technological</strong><p>Can models, platforms and vendors be replaced without losing capability?</p><b>↗</b></a><a href="taxonomy/ONTOLOGY.html"><span>04</span><strong>Legal</strong><p>Which entities, laws, obligations and contracts govern the system?</p><b>↗</b></a></div>
      <div class="manifesto"><span class="quote-mark">“</span><p>A sovereignty claim without a control and an evidence trail is a hypothesis, not an assurance.</p><span class="manifesto-foot">COURSE PRINCIPLE / A DECISION FRAMEWORK, NOT AN OFFICIAL STANDARD</span></div>
    </div>
    <div class="reading-section chapter-preview"><div class="section-intro"><span class="section-number">02 / AN OPEN CHAPTER</span><h2>A worked example, not a brochure.</h2><p>Begin with Module 01: a sourced introduction to enterprise control, concrete classification and testable sovereignty claims.</p></div>
      <a class="chapter-feature" href="modules/01-sovereign-ai-fundamentals.html"><div class="feature-index"><span>PART I</span><span>01</span></div><div class="feature-copy"><div class="feature-type">FIRST PUBLISHED CHAPTER <span>·</span> FOUNDATIONS</div><h3>Who controls the intelligence?</h3><p>Classify a sovereignty claim. Inspect dependencies and evidence. Run the local lab. Make the product decision.</p><span class="feature-action">Read chapter 01 <b>↗</b></span></div></a>
      <div class="after-feature"><a href="onboarding/index.html">Try the Decision Studio <span>↗</span></a><a href="taxonomy/ONTOLOGY.html">Explore the ontology <span>↗</span></a><a href="social/module-01/CAROUSEL.html">View the HTML question deck <span>↗</span></a><a href="curriculum.html">Browse all 24 modules <span>↗</span></a></div>
    </div>'''

def main():
    if DIST.exists(): shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    shutil.copytree(ROOT/'site/assets', DIST/'assets')
    for name in ['diagrams','labs','social','onboarding']:
        if (ROOT/name).exists():
            shutil.copytree(ROOT/name, DIST/name, ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    (DIST/'taxonomy').mkdir(exist_ok=True)
    shutil.copy2(ROOT/'taxonomy/ontology.yaml',DIST/'taxonomy/ontology.yaml')
    write(DIST/'index.html',frame(home(),'index','Opening pages'))
    paths=[
      ('TOC.md','curriculum.html','curriculum','Complete contents'),
      ('taxonomy/ONTOLOGY.md','taxonomy/ONTOLOGY.html','ontology','Taxonomy & ontology'),
      ('STYLE_GUIDE.md','editorial.html','editorial','Editorial standards'),
      ('CHAPTER_TEMPLATE.md','CHAPTER_TEMPLATE.html','editorial','Chapter template'),
      ('chapters/05-laws-regulation-jurisdiction.md','modules/05-laws-regulation-jurisdiction.html','module','Module 05'),
      ('chapters/01-sovereign-ai-fundamentals.md','modules/01-sovereign-ai-fundamentals.html','module01','Module 01'),
      ('labs/module-01/README.md','labs/module-01/index.html','module01','Module 01 lab'),
      ('social/module-01/POST.md','social/module-01/POST.html','module01','LinkedIn post draft 01'),
      ('social/module-05/SLIDES.md','social/module-05/SLIDES.html','module','Question deck outline'),
      ('social/module-05/POST.md','social/module-05/POST.html','module','LinkedIn post draft'),
      ('labs/module-05/README.md','labs/module-05/index.html','module','Module 05 lab'),
    ]
    for source,dest,page,title in paths:
        if not (ROOT/source).exists():
            continue
        content,sections=article_content(ROOT/source,dest,diagram=(page=='module' and source.startswith('chapters/') and source.startswith('chapters/05')))
        if page=='curriculum':
            soup=BeautifulSoup(content,'html.parser')
            for h in soup.find_all('h3'):
                m=re.match(r'Module (\d{2})',h.get_text())
                if m:h['id']=f'module-{m.group(1)}'
            content=str(soup)
        prefix='../'*dest.count('/')
        write(DIST/dest,frame(content,page,title,prefix,True,sections))
    # Custom-designed HTML carousels, independent of Markdown rendering.
    for n in ('01','05'):
        if (ROOT/f'social/module-{n}/CAROUSEL.html').exists():
            shutil.copy2(ROOT/f'social/module-{n}/CAROUSEL.html',DIST/f'social/module-{n}/CAROUSEL.html')
    print('Built',len(list(DIST.rglob('*.html'))),'HTML pages in', DIST)

if __name__=='__main__':main()