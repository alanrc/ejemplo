var tabla = "#tabla_categoria"; 
var boton_eliminar = ".delete"; 
var formulario_modal = "#form_eliminar";
var ventana_modal = "#myModal"; 

    $(document).on('ready',function(){
        $(boton_eliminar).on('click',function(e){
            e.preventDefault();
            var catid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idCategoria').val(catid);
            $('#modal_name').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        alert("Eliminado!");
                        var idCat = response.product_id;
                        var elementos= $(tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(ventana_modal).modal('hide');
                        }
                        
                    }else{
                        alert("Hubo un error al eliminar!");
                        $(ventana_modal).modal('hide');
                    };
                }
            };

        $(formulario_modal).ajaxForm(options);
    });