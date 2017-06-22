$(document).on("ready",inicio);

function inicio () {
	$("span.help-block").hide();
	$('#btnvalidar').click(function () {
		if (validar() == false)
			alert("los campos no estan validados");
		else {
			alert("los campos estan validados")
		}
	});
	$("#texto").keyup(validar);
}

function validar () {
	var valor = document.getElementById("texto").value;
	if (valor == null || valor.length == 0 || /^\s+$/.test(valor)) {
		$("#icontext").remove();
		$("#texto").parent().parent().attr("class","form-group has-error has-feedback")
		$("#texto").parent().children("span").text("debe ingresar algun caracter").show();
		$("#texto").parent().append("<span id='icontext' class='glyphicon glyphicon-remove form-control-feedback'></span>");
		return false;
	} else if (isNaN(valor)) {
		$("#icontext").remove();
		$("#texto").parent().parent().attr("class","form-group has-error has-feedback")
		$("#texto").parent().children("span").text("debe ingresar caracteres numericos").show();
		$("#texto").parent().append("<span id='icontext' class='glyphicon glyphicon-remove form-control-feedback'></span>");
		return false;
	}
	else {
		$("#icontext").remove();
		$("#texto").parent().parent().attr("class","form-group has-success has-feedback")
		$("#texto").parent().children("span").text("debe ingresar algun caracter").hide();
		$("#texto").parent().append("<span id='icontext' class='glyphicon glyphicon-ok form-control-feedback'></span>");
		return true;
	}
}