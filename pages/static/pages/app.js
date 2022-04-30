function myFunction(genre) {
  console.log(genre);
  localStorage.setItem('genre', genre);
    //   $.ajax({
    //     type: 'POST',
    //     headers: {'X-CSRFToken': csrftoken},
    //     data:{
    //       x:genre
    //     },
    //     dataType:'json',
    // });
}
