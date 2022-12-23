function SendPassword()
{
   let user_password = document.getElementById("password").value;
    let password={"password":user_password}
    axios.post("http://127.0.0.1:5000/password-checker", password)
        .then((res) => {
            console.log(res.data.response)
        })
        .catch((err) => {
        console.log(err)
        })
  

    

}