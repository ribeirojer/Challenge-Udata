import First from "./components/First";
import Second from "./components/Second";
import Third from "./components/Third";
import PieChart from "./components/PieChart";
import MapChart from "./components/MapChart";
import DiffChart from "./components/DiffChart";
import "./App.css";
import data from "../saida.json";
import os_20_paises from "../os_20_paises.json";
import os_20_produtos from "../os_20_produtos.json";

interface IDados {
  Mês: string;
  "País Importado": string;
  Produto: string;
  Via: string;
  "FOB (US$)": string;
}

function App() {

  return (
    <div className="App">
      <First namedata="País" title="os_20_paises" dados={os_20_paises}></First>
      <First namedata="País" title="os_20_produtos" dados={os_20_produtos}></First>
      <Second></Second>
      <Third></Third>
      <PieChart></PieChart>
      <MapChart></MapChart>
      <DiffChart></DiffChart>
    </div>
  );
}

export default App;
