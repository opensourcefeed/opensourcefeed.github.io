$(function () {

    // Filter the results on keyup
    $('#search-field').on('keyup', function () {

        var query = $(this).val();
        var entryParent = $('#result-list');
        var entries = $(entryParent).find('li').not('#no-result');
        var hasResult = false;
        var noResult = $('#no-result');

        if (query != undefined && query != '') {
            $(entries).each(function () {
                if ($(this).text().toLowerCase().indexOf(query.toLowerCase()) == -1) {
                    $(this).hide();
                } else {
                    hasResult = true;
                    $(this).show();
                }
            });
            if (hasResult) {
                $(noResult).hide();
            } else {
                $(noResult.show());
                hasResult = true;
            }
        }

        if (hasResult) {
            $(entryParent).width($(this).innerWidth() - 1)
                .css('margin-left', $('#search-btn').parent().width())
                .show();
        } else {
            $(entryParent).hide();
        }
    });

    var closeSearch = function () {
        $('#search-field').val('');
        $('#search-field').trigger('keyup');
    }
    // Close the search result, when clicking outside
    $(':not("#search-area")').on('click', closeSearch);
    $(document).keyup(function (e) {
        if (e.key === 'Escape') {
            closeSearch();
        }
    });

    // Control size of navbar on scrolling
    $(window).scroll(function () {
        if ($(document).scrollTop() > 50) {
            $('.navbar').addClass('navbar-small');
            $('main').css('margin-top', '100px');
        }
        else {
            $('.navbar').removeClass('navbar-small');
            $('main').removeAttr('style');
        }

        if ($(window).width() > 768) {
            var elem = $('aside ins.adsbygoogle');
            if (elem.length) {
                if ($(document).scrollTop()) {
                    elem.css('position', 'fixed');
                    elem.css('top', 114);
                } else {
                    elem.css('position', 'relative');
                }
            }
        }
    });
});
