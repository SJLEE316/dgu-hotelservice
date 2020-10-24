// function form_btn(n){
//     var text = document.getElementById("text");
//     text_val = parseInt(text.value);
//     text_val += n;
//     text.value = text_val;
//     if(text_val<=0){
//         text.value=1;
//     }
// }

// function form_btn2(n){
//     var text = document.getElementById("text2");
//     text_val = parseInt(text.value);
//     text_val += n;
//     text.value = text_val;
//     if(text_val<=0){
//         text.value=1;
//     }

//     countPrice();
// }

var count1 = 1;
var countEl = document.getElementById("count1");
var total_count = document.getElementById("total_count"); //추가
var total_count_view = document.getElementById("total_count_view"); //추가

function plus(){
  count1++;
  countEl.value = count1;
  total_count_view.value = total_count.value * countEl.value; //추가
}
function minus(){
  
  if (count1 > 1) {
    count1--;
    countEl.value = count1;
    total_count_view.value = total_count_view.value - total_count.value; //추가  
  }  
}

var count2 = 1;
var countEl2 = document.getElementById("count2");
var total_count2 = document.getElementById("total_count2"); //추가
var total_count_view2 = document.getElementById("total_count_view2"); //추가

function plus2(){
  count2++;
  countEl2.value = count2;
  total_count_view2.value = total_count2.value * countEl2.value; //추가
}
function minus2(){
  
  if (count2 > 1) {
    count2--;
    countEl.value2 = count2;
    total_count_view2.value = total_count_view2.value - total_count2.value; //추가  
  }  
}