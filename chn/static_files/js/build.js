$("#province").change(function(){
    var province = $(this).val();
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
$("button").click(function(){
   var province = $("#province").val();
   var city = $("#city").val();
   var county = $("#county").val();
   var sex = $("#sex").val();
   var birthday_code = $("#birthday_code").val();
   alert(province+city+county+sex+birthday_code);
   $.ajax({
        url: '/id/get/',
        data:{"province":$("#province").val(),
              "city":$("#city").val(),
              "county":$("#county").val(),
              "sex":$("#sex").val(),
              "birthday_code":$("#birthday_code").val(),
              "id_quantity":$("#id_quantity").val()
              },
        type: 'POST',
        dataType: 'json',
        success: function (data){
            var content='';
            $.each(data, function(i, item){
                content+='<br/>'+item
            });
            $('#num_list').html(content)
        }
   });
});

