var time=0;
var c=0;

function ShowDetail(x,length) {
	$(document).ready(function(){
		if (time==0){
			for (var i=1; i<=length; i++) {
				var title='learn_title_'+i;
				var detail='learn_detail_'+i;
				var img='learn_img_'+i;
				var download='learn_download_'+i;
				if(title==x.id){
					$('#'+detail).animate({height: "400px"});
					$('#'+detail).css('overflow','visible');					
					$('#'+img).css('display','block');
					$('#'+download).css('display','block');
				}				
				else{
					$('#'+title).fadeOut('fast');
					$('#'+detail).fadeOut('fast');
				}
			}
			time=1;
		}
		else if (time==1) {
			for (var i=1; i<=length; i++) {
				var title='learn_title_'+i;
				var detail='learn_detail_'+i;
				var img='learn_img_'+i;
				var download='learn_download_'+i;
				if(title==x.id){
					$('#'+detail).animate({height: "30px"});
					$('#'+detail).css('overflow','hidden');
					$('#'+img).css('display','none');
					$('#'+download).css('display','none');					
				}				
				else{
					$('#'+title).fadeIn('fast');
					$('#'+detail).fadeIn('fast');
				}
			}
			time=0;		
		}
	})
}

function SchedulePanel() {
	$(document).ready(function(){
		var schedule='schedule_table';
		var list='cover_list'
		if(c==0){
			$('#'+schedule).animate({height: "300px"});
			$('#'+list).animate({margin:"20px 0 0 0"});
			$('#'+schedule).css('display','block');					
			c=1;
		}
		else {
			$('#'+schedule).animate({height: "0px"},function(){
				$('#'+schedule).css('display','none');
			});
			$('#'+list).animate({margin:"160px 0 0 0"});					
			c=0;
		}
	})	
}

function commentSubmit(){
	document.getElementById('comment').submit();
}

function Download(url){
	var aLink = document.createElement('a');
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent("click", false, false);
    aLink.href = new URL(url,'http://127.0.0.1:8000/dosmis_zh_cn');
    aLink.dispatchEvent(evt);
    aLink.click();
}