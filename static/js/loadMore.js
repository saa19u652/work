const data = () => {
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
    return [array, array2, array3, array4]
}

$('#loadmoreBtn').click(function () {
    const info = data
    const count = $("tr").length - 1;
    const search =  $("#searchbar").val()
    $.ajax('/filter/', {
        method: 'POST',
        data: {
            date_from: $("#fromD").val(),
            date_to: $("#toD").val(),
            'materail[]': info[0],
            'tech[]': info[1],
            'location[]': info[2],
            'owner[]': info[3],
            wfrom: $("#fromW").val(),
            wto: $("#toW").val(),
            hfrom: $("#fromH").val(),
            hto: $("#toH").val(),
            offset: count,
            title: search
        },
        beforeSend:function (xhr, settings) {
            $('#loadmoreBtn').addClass("'disabled").text("Загрузка")
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    }).done(function (data) {
        table = $("#tbody-gallary");
        data.post.forEach(elem => {
            line = createTr(elem)
            table.append("<tr>" + line[0] + line[1] + line[2] + line[3] + line[4] + line[5] + line[6] + line[7] + line[8] + line[9] + "</tr>");
        });
        const count = $("tr").length - 1;
        if(count == data.totalResult) {
             $('#loadmoreBtn').hide()
        } else {
         $('#loadmoreBtn').removeClass("'disabled").text("Загрузить еще")
        }
    })
});

const createTr = (elem) => {
          let picS = ""
          if (elem.picS != null) {
             picS =  "<td><div id=\"thumbwrap\"><a class=\"thumb\" target=\"_blank\"  href=\"art/" + elem.pk + "/\"> <img src='/gallery_pic/" + elem.picS + "' alt='' class='pic'><span><img src='/gallery_pic/" + elem.picS + "' alt=''></span></a></div></td>"
          }

          let author__author = ""
          if (elem.author__author != null) {
             author__author = "<td>" + elem.author__author + "</td>"
          }

          let title = ""
          if (elem.title != null) {
             title = "<td>" + elem.title + "</td>"
          }

          let year = ""
          if (elem.year != null) {
             year = "<td>" + elem.year + "</td>"
          }

          let material__material = ""
          if (elem.material__material !== undefined) {
             material__material = "<td>" + elem.material__material + "</td>"
          }
          let paints__paints = ""
          if (elem.paints__paints !== undefined) {
             paints__paints = "<td>" + elem.paints__paints + "</td>"
          }

          let sizeWsizeH = ""
          if (elem.sizeW != null && elem.sizeH != null) {
             sizeWsizeH = "<td>"  + elem.sizeW + 'x' + elem.sizeH + "</td>"
          }

          let location__located = ""
          if (elem.location__located !== undefined) {
             location__located = "<td>" + elem.location__located + "</td>"
          }

          let owner = ""
          if (elem.owner__owner !== undefined) {
             owner =  "<td>" + elem.owner__owner + "</td>"
          }

          let comment = ""
          if (elem.comment != null) {
             comment = "<td>" + elem.comment + "</td>"
          }

          return [picS, author__author, title, year, material__material, paints__paints, sizeWsizeH, location__located, owner, comment]
}