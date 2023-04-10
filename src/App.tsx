import First from "./components/First";
import Second from "./components/Second";
import PieChart from "./components/PieChart";
import MapChart from "./components/MapChart";
import DiffChart from "./components/DiffChart";
import "./App.css";
import os_20_paises from "../os_20_paises.json";
import os_20_produtos from "../os_20_produtos.json";
import vias_por_mes from "../vias_por_mes.json";
import paises_ordenados from "../paises_ordenados.json"

function App() {
  return (
    <div className="App">
      <First namedata="País" title="os_20_paises" dados={os_20_paises}></First>
      <PieChart dados={os_20_produtos}></PieChart>
      <Second dados={vias_por_mes}></Second>
      <DiffChart></DiffChart>
      <MapChart data={paises_ordenados}></MapChart>
    </div>
  );
}

export default App;
