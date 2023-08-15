// create FizzBuzzList component that takes in fizzBuzzAraay as prop and maps through it to list the items

//import bootstrap compoent
import ListGroup from 'react-bootstrap/ListGroup';
import "./FizzBuzzList.css"

function FizzBuzzList({fizzBuzzArray}) {

    return (
        <ListGroup>
        <h1 className="fizzbuzz-title">FizzBuzz</h1>
            {fizzBuzzArray.map((item, index) => {
                return <ListGroup.Item 
                key={index}
                className={item === "Fizz" ? "fizz" : item === "Buzz" ? "buzz" : item === "FizzBuzz" ? "fizzbuzz" : ""}
                >{item}</ListGroup.Item>
            })}
        </ListGroup>
    )
}

export default FizzBuzzList;