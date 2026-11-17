(() => {
  const btn = document.querySelector('.mobile-toggle');
  const nav = document.querySelector('.header-nav');
  if (btn && nav) btn.addEventListener('click', () => {
    const opened = nav.classList.toggle('show');
    btn.setAttribute('aria-expanded', String(opened));
  });
  const search = document.querySelector('#module-search');
  if (search) search.addEventListener('input', () => {
    const query = search.value.trim().toLowerCase();
    document.querySelectorAll('[data-module-title]').forEach(el => {
      el.hidden = !el.getAttribute('data-module-title').toLowerCase().includes(query);
    });
  });
})();