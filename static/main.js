jQuery(function () {
  const $ssr = $("[data-ssr]");
  const $searcherLists = $("[data-searcher]");

  const serverAction = function () {
    const $objective = $(this);
    const { event, listener } = $objective.data();
    if (!event || !listener) return;
    const $listener = $(listener);
    $listener.on(event, function (e) {
      e.preventDefault();
      const $element = $(this);
      const {
        action = $element.attr("action"),
        method = $element.attr("method"),
      } = $element.data();
      let formData = null;

      if ($element.is("form")) {
        formData = new FormData(this);
      } else if ($element.attr(value)) {
        formData = new FormData();
        const name = $element.attr("name");
        const value = $element.attr("value");
        formData.append(name, value);
      }

      $.ajax({
        url: action,
        type: method,
        data: formData,
        dataType: "html",
        processData: false,
        contentType: false,
        success: (content) => {
          $objective.html(content)
          const $parent = $objective.parent();
          const $renew = $parent.find('[data-ssr]');
          $renew.each(serverAction);
        },
        error: (error) => console.error(error),
      });
    });
  };

  $ssr.each(serverAction);

  $searcherLists.on("click", "> *", function () {
    const $this = $(this);
    const value = $this.val() ? $this.val() : $this.data("value");
    const name = $this.data("name") ? $this.data("name") : $this.text().trim();
    const $list = $this.parent();
    const { target } = $list.data();
    const $input = $list.parent().find("input.searcher");
    const $target = $(target);
    $list.children().remove();
    $target.attr("value", value);
    $input.val(name);
  });
});
