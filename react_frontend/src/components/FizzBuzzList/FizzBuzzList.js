// create FizzBuzzList component that takes in fizzBuzzAraay as prop and maps through it to list the items

function FizzBuzzList({fizzBuzzArray}) {

    return (
        <ul>
            {fizzBuzzArray.map((item, index) => {
                return <li key={index}>{item}</li>
            })}
        </ul>
    )
}

export default FizzBuzzList;