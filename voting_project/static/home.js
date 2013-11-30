var voter = undefined
var discussion = undefined

var voter_id = undefined
var discussion_id = undefined

$(document).ready(function(){

    $('select').selectpicker();
    $('#voter').selectpicker('val', 'null')
    $('#discussion').selectpicker('val', 'null')

    $("#btn-up").click(function(){

        if((discussion == undefined) || (voter == undefined)) return;
        console.log("up vote from " + voter + " in " + discussion_id + " discussion")

        $.post('/vote/', {'voter': voter, 'discussion': discussion, 'vote': +1.0})
    });

    $("#btn-down").click(function(){

        if((discussion == undefined) || (voter == undefined)) return;
        console.log("down vote from " + voter + " in " + discussion_id + " discussion")

        $.post('/vote/', {'voter': voter, 'discussion': discussion, 'vote': -1.0})
    })

    $('#voter').on('change', function(){

        voter = $("[data-id='voter']").next().find('li').filter(".selected").find('span')[0].innerText
        console.log("new voter " + voter)

        voter_id = $('#voter option').filter(function () { return $(this).html() == voter; }).attr('value')
        console.log("voter id: " + voter_id)
    })

    $('#discussion').on('change', function(){

        discussion = $("[data-id='discussion']").next().find('li').filter(".selected").find('span')[0].innerText
        console.log("new discussion " + discussion)

        discussion_id = $('#discussion option').filter(function () { return $(this).html() == discussion; }).attr('value')
        console.log("discussion id: " + discussion_id)
    })
});