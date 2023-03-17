$(document).on('click', '#delete_employee', function(){
    var ans = window.confirm('Are you sure you want to delete this employee?');
    if(ans){
        return true;
    }else{
        return false;
    }
});