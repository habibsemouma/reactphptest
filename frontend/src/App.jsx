import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import axios from "axios";
import "./styles/home.css";
import Monster from "./assets/monster.jpeg";

function App() {
    const [data, setData] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
            try {
                // Make a GET request using Axios
                const response = await axios.get("http://localhost:8000/");

                // The response data is already parsed as JSON, so you can directly use it
                const result = response.data;

                // Update the state with the fetched data
                setData(result);

                console.log(result);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        // Call the fetchData function
        fetchData();
    }, []);

    return (
        <div>
            <h1>Big test</h1>
            <div id="data-wrapper">
                {data.map((item) => (
                    <div class="card" key={item.id}>
                        <img src={Monster}></img>
                        <div className="card-text-part">
                            <p>Name: {item.name}</p>
                            <p>Age: {item.age}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
