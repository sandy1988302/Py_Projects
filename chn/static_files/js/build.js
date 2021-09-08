//function main() {
//    alert("开始");
//    $("button").click(function(){
//        alert("值为: " + $("#province").val());
//    });
//}
$("#province").change(function(){
    var province = $(this).val();
    alert("province改变了");
    $.ajax({
        url: '/id/get_city/',
        data:{"province":$(this).val()},
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            var content='';
            $.each(data, function(i, item){
                content+='<option value='+item.city_name+'>'+item.city_name+'</option>'
            });
            $('#city').html(content)
        },
    });
});
$("#city").change(function(){
    var city = $(this).val();
    alert("city改变了");
    $.ajax({
        url: '/id/get_county/',
        data:{"city":$(this).val()},
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            var content='';
            $.each(data, function(i, item){
                content+='<option value='+item.county_name+'>'+item.county_name+'</option>'
            });
            $('#county').html(content)
        },
    });
});

