var dict = {}
var rowCount = 0;

function deleteRow(event){
row = event.target.closest('tr')
//index = $('table[id = orders] tbody tr').index(row) - 2
id = dict[row.id]
row.remove()
delete dict[row.id]
rowCount--
for(var key in dict){
if(dict[key] > id)
    dict[key] = dict[key] - 1;
    }
if(rowCount == 0)
 {
    $('#orderWrapper').toggleClass('invisible')
    $('#auth_hint').toggleClass('invisible')
 }
}

async function Save(){
var trs = $('table[id=orders] tbody tr')
  var context = [];
for(var index = 2; index < trs.length; index++)
    {
        id = parseInt(trs[index].id)
        quantity = parseInt(trs[index].cells[2].innerHTML)
        let obj = {
        id: id,
        quantity: quantity
        }
        context.push(obj)
    }
     if(context.length != 0)
    {
        context = JSON.stringify(context)
        console.log(context)

        let csrftoken = getCookie('csrftoken');

        let response = await fetch('create_order/', {
        method: 'POST',
        mode: 'cors',
        referrerPolicy: 'strict-origin-when-cross-origin',
        body: context,
        headers: {
        "X-CSRFToken": csrftoken
        },
        credentials: 'same-origin'
        })

        location.href = "../account/"
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
                }
            }
    }
return cookieValue;
}

$(document).ready(function(){
$('#orderWrapper').toggleClass('invisible')
$('table[id = prods] tr td label').click(function (event){

price_value = this.closest('tr').cells[1].innerHTML

if(this.id in dict){
num = dict[this.id]
var cur = $('tr', 'table[id=orders]').eq(2 + num)
quantity = cur[0].cells[2].innerHTML
cur[0].cells[2].innerHTML = parseInt(quantity) + 1
return
}
else{
dict[this.id] = rowCount
if(rowCount == 0){
 $('#orderWrapper').removeClass('invisible')
 $('#auth_hint').addClass('invisible')
    }
rowCount++
}

markup = '<tr id='+this.id+'>'
name = '<td>' + this.innerHTML + '</td>'
price = '<td>' + price_value + '</td>'
quant = '<td>' + 1 + '</td>'
del = '<td><button class="btn btn-danger" id="but_del" onclick="deleteRow(event)">' + "Delete" + '</button></td>'

markup += name + price + quant + del + '</tr>'

tbody = $('table[id=orders] tbody')

tbody.append(markup)
})
})

