import { useState } from "react";
import First from "./components/First";
import Second from "./components/Second";
import Third from "./components/Third";
import PieChart from "./components/PieChart";
import MapChart from "./components/MapChart";
import DiffChart from "./components/DiffChart";
import "./App.css";
import data from "./assets/data.json"

function App() {
  const [count, setCount] = useState(data);

  return (
    <div className="App">
      <First></First>
      <Second></Second>
      <Third></Third>
      <PieChart></PieChart>
      <MapChart></MapChart>
      <DiffChart></DiffChart>
    </div>
  );
}

export default App;
