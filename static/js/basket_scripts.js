window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var target_input = event.target;

        $.ajax({
            url: "/basket/edit/" + target_input.name + "/?quantity=" + target_input.value,


        });

        event.preventDefault();
    });
};
