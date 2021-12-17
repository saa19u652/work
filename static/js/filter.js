
$('#searchbar_pic').click(function () {
    const array = [];
    $("input:checkbox[name=material]:checked").each(function () {
        array.push($(this).val());
    });
    const array2 = [];
    $("input:checkbox[name=paints]:checked").each(function () {
        array2.push($(this).val());
    });
    const array3 = [];
    $("input:checkbox[name=places]:checked").each(function () {
        array3.push($(this).val());
    });
    const array4 = [];
    $("input:checkbox[name=owner]:checked").each(function () {
        array4.push($(this).val());
    });

    $.ajax('/filter/', {
        method: 'POST',
        data: {
            date_from: $("#fromD").val(),
            date_to: $("#toD").val(),
            'materail[]': array,
            'tech[]': array2,
            'location[]': array3,
            'owner[]': array4,
            wfrom: $("#fromW").val(),
            wto: $("#toW").val(),
            hfrom: $("#fromH").val(),
            hto: $("#toH").val(),
            title: $("#searchbar").val(),
        }
    }).done(function (data) {
        reloadTable(data);
    })
})

$('.filter').click(function () {
    const array = [];
    $("input:checkbox[name=material]:checked").each(function () {
        array.push($(this).val());
    });
    const array2 = [];
    $("input:checkbox[name=paints]:checked").each(function () {
        array2.push($(this).val());
    });
    const array3 = [];
    $("input:checkbox[name=places]:checked").each(function () {
        array3.push($(this).val());
    });
    const array4 = [];
    $("input:checkbox[name=owner]:checked").each(function () {
        array4.push($(this).val());
    });
    $.ajax('/filter/', {
        method: 'POST',
        data: {
            date_from: $("#fromD").val(),
            date_to: $("#toD").val(),
            'materail[]': array,
            'tech[]': array2,
            'location[]': array3,
            'owner[]': array4,
            wfrom: $("#fromW").val(),
            wto: $("#toW").val(),
            hfrom: $("#fromH").val(),
            hto: $("#toH").val(),
        }
    }).done(function (data) {
        $("#searchbar").val('')
        reloadTable(data)
    })
});

function reloadTable(data) {
    let table = document.getElementById("tableid");

    for (let i = table.rows.length - 1; i > 0; i--) {
        table.deleteRow(i);
    }

    table = $("#tbody-gallary");
    $('#loadmoreBtn').show()
    data.post.forEach(elem => {
        const line = createTr(elem)
        table.append("<tr>" + line[0] + line[1] + line[2] + line[3] + line[4] + line[5] + line[6] + line[7] + line[8] + line[9] + "</tr>");
    });
}


