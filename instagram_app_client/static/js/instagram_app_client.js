"use strict";

function initInstagramStream() {
    $(".fancybox")
        .attr('rel', 'gallery')
        .fancybox({
            beforeLoad: divAsTitle,
            afterShow: setTitleMargin
        });
}

function divAsTitle() {
    var el, id = $(this.element).data('title-id');

    if (id) {
        el = $('#' + id);

        if (el.length) {
            this.title = el.html();
        }
    }
}

function setTitleMargin(marginBottom) {
    var activeImage = $($('.fancybox-opened .fancybox-title')[0]);

    marginBottom = marginBottom || 20;
    marginBottom = -activeImage.outerHeight() - marginBottom;
    activeImage.css('margin-bottom', marginBottom)
}

document.addEventListener('DOMContentLoaded', initInstagramStream);
