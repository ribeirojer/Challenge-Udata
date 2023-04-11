import First from "./components/First";
import Second from "./components/Second";
import PieChart from "./components/PieChart";
import MapChart from "./components/MapChart";
import DiffChart from "./components/DiffChart";
import "./App.css";
import os_20_paises from "../outputs/os_20_paises.json";
import os_20_produtos from "../outputs/os_20_produtos.json";
import vias_por_mes from "../outputs/vias_por_mes.json";
import paises_ordenados from "../outputs/paises_ordenados.json";
import Table from "./components/Table";
import correlacao_vias from "../outputs/correlacao_vias.json";

function App() {
  return (
    <div className="App">
      <First
        namedata="País"
        title="Os 20 principais países exportadores"
        dados={os_20_paises}
      ></First>
      <PieChart
        title="Os 20 principais produtos importados"
        dados={os_20_produtos}
      ></PieChart>
      <Second dados={vias_por_mes}></Second>
      <Table data={correlacao_vias} data_correlacao={0}></Table>
      <DiffChart></DiffChart>
      <MapChart data={paises_ordenados}></MapChart>
    </div>
  );
}

export default App;
