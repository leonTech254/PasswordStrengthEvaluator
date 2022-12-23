// Create the element outside of the function
let mylist = document.createElement('li');
let result_container = document.querySelector(".result");
result_container.appendChild(mylist);
mylist.classList.add("error")
function SendPassword() {
  let user_password = document.getElementById("password").value;

  // Update the element's content or properties within the function
  let password = {"password": user_password};
  axios.post("https://api.leonteqsecurity.com/password-checker", password)
    .then((res) => {
      let password_report = res.data.response;
      mylist.textContent = "";
        for (let key in password_report) {
            if (key == "weaknesses")
            {   mylist.innerHTML+="PASSWORD WEAKNESSES"
                mylist.innerHTML+="<ul>"
                for (let i = 0; i < password_report[key].length; i++)
                {
                    password_report[key][i]
                    mylist.innerHTML+="<li>"+password_report[key][i]+"</li>"

                    
                }
                mylist.innerHTML+="</ul>"
                
                
            } else
            {
                 mylist.innerHTML+= key + " " + " " + password_report[key] + "<br>";
                
            }
              
       
      }
    })
    .catch((err) => {
      console.log(err)
    });
}
