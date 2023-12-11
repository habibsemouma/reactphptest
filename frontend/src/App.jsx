import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";
import "./styles/home.css";
import Monster from "./assets/monster.jpeg";

function App() {
    const [data, setData] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get("/endpoint1");

                const result = response.data;

                setData(result);

                console.log(result);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

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
                            <p>Name: {item.name +' a'} </p>
                            <p>Age: {item.age}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
