const del_btn = document.getElementById('deleteuseraccount');

del_btn.click(function(){
    swal({
        title: 'Delete Account',
        text: 'Are you sure you want to delete your account. This cannot be reversed!',
        icon: 'danger',
        confirmationButtonText:'DELETE'
    })
    
})