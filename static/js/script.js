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
}

function Save(){
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

        fetch('create_order/', {
        method: 'POST',
        mode: 'cors',
        referrerPolicy: 'strict-origin-when-cross-origin',
        body: context
        })
    }
}

$(document).ready(function(){
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

