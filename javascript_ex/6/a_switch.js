// 1.

// let confirmed = confirm("Do u want to delete this page?")

// switch(confirmed){
//     case true:
//         alert("Page deleted");
//         break;
    
//     case false:
//         alert("Page not deleted");
//         break;
// }


// 2.


let dayNum = prompt("Enter num of day in week: ")

switch(dayNum) {
    case "1":
    case "2":
    case "3":
    case "4":
    case "5":
        alert("Work day")
    
    case "6":
    case "7":
        alert("Free day")

    default:
        alert("Error")
    
}