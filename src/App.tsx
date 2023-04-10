import { useState } from "react";
import First from "./components/First";
import Second from "./components/Second";
import Third from "./components/Third";
import PieChart from "./components/PieChart";
import MapChart from "./components/MapChart";
import DiffChart from "./components/DiffChart";
import "./App.css";
import data from "../saida.json";

interface IDados {
  Ano: string;
  Mês: string;
  "País Importado": string;
  Produto: string;
  "UF Importadora": string;
  Via: string;
  "FOB (US$)": string;
}

function App() {
  const dados:IDados = data
  const [count, setCount] = useState(dados);

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
