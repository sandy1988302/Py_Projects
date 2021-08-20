$(main);
        function main() {
            var $province = $("#province")
            sendProvinceAjax();
            $province.change(provinceChange)
        }
        function sendProvinceAjax(){
            $.get("/id/province/",function(data){
                console.log(data);
                $.each(data.d,function(idx,val){
                    var id=val[0];
                    var name=val[1];
                    var option="<option value="+id+">"+name+"</option>";
                    $province.append(option);
                });
            })
        };


        $("province").change(function(){
            var province=$(this).val();
            alert("操作省份变动");
//            $.ajax({
//                url:'/id/get_city/',
//                date:{"province":$(this).val()},
//                type:'GET',
//                dataType:'json',
//                success:function(data){
//                    var content='';
//                    $.echo(data,function(i,item){
//                        content+='<option value='+item.city_name+'>'+item.city_name+'<option>'
//                    });
//                    $('#city').html(content)
//                },
//            });
        });
