/* Search all text titles, descriptions, explicit summaries and tags in the current language. */
(() => {
    const box = document.querySelector('[data-text-search]');
    if (!box) return;
    const input = box.querySelector('input');
    const results = box.querySelector('[data-search-results]');
    const status = box.querySelector('[data-search-status]');
    const rows = [...results.querySelectorAll('li')];
    const regular = [...document.querySelectorAll('main > article.post-entry, main > footer.page-footer')];
    const normalize = value => value.toLocaleLowerCase().replace(/ё/g, 'е').normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    const index = rows.map(row => ({row, value: normalize(row.dataset.search || '')}));
    function update() {
        const terms = normalize(input.value).trim().split(/\s+/).filter(Boolean);
        const searching = terms.length > 0;
        let count = 0;
        for (const entry of index) {
            const match = searching && terms.every(term => entry.value.includes(term));
            entry.row.hidden = !match;
            if (match) count++;
        }
        results.hidden = !searching;
        for (const item of regular) item.hidden = searching;
        status.textContent = searching ? `${status.dataset.label}: ${count}` : '';
    }
    box.hidden = false;
    input.addEventListener('input', update);
    input.addEventListener('search', update);
    update();
})();
