document.addEventListener("DOMContentLoaded", function () {

    const searchField = document.getElementById('search-field');

    if (searchField) {
        // Filter the results on keyup
        document.getElementById('search-field').addEventListener('keyup', function () {
            const query = this.value;
            const entryParent = document.getElementById('result-list');
            const entries = entryParent.querySelectorAll('li:not(#no-result)');
            let hasResult = false;
            const noResult = document.getElementById('no-result');

            if (query !== undefined && query !== '') {
                entries.forEach(function (entry) {
                    if (entry.textContent.toLowerCase().indexOf(query.toLowerCase()) === -1) {
                        entry.style.display = 'none';
                    } else {
                        hasResult = true;
                        entry.style.display = '';
                    }
                });

                if (hasResult) {
                    noResult.style.display = 'none';
                } else {
                    noResult.style.display = '';
                }
            }

            if (hasResult) {
                entryParent.style.width = (this.offsetWidth - 1) + 'px';
                entryParent.style.marginLeft = document.getElementById('search-btn').offsetWidth + 'px';
                entryParent.style.display = 'block';
            } else {
                entryParent.style.display = 'none';
            }
        });

        const closeSearch = function () {
            const searchField = document.getElementById('search-field');
            searchField.value = '';
            searchField.dispatchEvent(new Event('keyup'));
        };

        // Close the search result when clicking outside
        document.body.addEventListener('click', function (e) {
            if (!document.getElementById('search-area').contains(e.target)) {
                closeSearch();
            }
        });

        document.addEventListener('keyup', function (e) {
            if (e.key === 'Escape') {
                closeSearch();
            }
        });
    }

    // Control size of navbar on scrolling
    window.addEventListener('scroll', function () {
        const navbar = document.querySelector('.navbar');
        const main = document.querySelector('main');
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;

        if (scrollTop > 50) {
            navbar.classList.add('navbar-small');
            main.style.marginTop = '100px';
        } else {
            navbar.classList.remove('navbar-small');
            main.removeAttribute('style');
        }

        if (window.innerWidth > 768) {
            const elem = document.querySelector('aside ins.adsbygoogle');
            if (elem) {
                if (scrollTop > 0) {
                    elem.style.position = 'fixed';
                    elem.style.top = '20px';
                } else {
                    elem.style.position = 'relative';
                }
            }
        }
    });

});
