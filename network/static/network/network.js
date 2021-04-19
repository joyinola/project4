// const strong=document.querySelector('#like_count');
document.addEventListener('DOMContentLoaded', ()=>{
// const strong=document.querySelector('strong');

document.querySelectorAll('.likes').forEach(item=>{item.addEventListener('click', ()=>{
	likee(item.dataset.name)}
	)}
	);
})


function likee(post_id)
{

	// document.querySelector('#likes').onclick(
	// ()=>{})
	fetch(`/like/${post_id}`).then(response=>response.json()).then(data=>
	{
    	 document.querySelector(`#like_count${post_id}`).innerHTML=data['like'];
    	 document.querySelector(`#like${post_id}`).innerHTML=data['text']
    })};


