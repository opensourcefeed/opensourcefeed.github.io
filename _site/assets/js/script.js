$(function() {
	function searchFunc() {
	  var query = $(this).val();
	  var parent = $(this).parent().parent().parent();
	  var entryParent = $(parent).next().next();
	  var entries = $(entryParent).find('a');
	  var hasResult = false;
	  $(entries).each(function() {
	  	if ($(this).text().toLowerCase().indexOf(query.toLowerCase()) == -1) {
	  		$(this).hide();
	  	} else {
	  		hasResult = true;
	  		$(this).show();
	  	}
	  });
	  
	  if (hasResult) {
	  	$(entryParent).next().hide();
	  } else {
	  	$(entryParent).next().show();
	  }
	}
	
	$('#searchos').keyup(searchFunc);
	$('#searchdesktop').keyup(searchFunc);
	
});


