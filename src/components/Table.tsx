import React from "react";

type Props = {
  data: any;
  data_desvio: any;
};

const Table = ({ data, data_desvio }: Props) => {
  function formattedPrice(value: number) {
    return value.toLocaleString("en-US", {
      currency: "USD",
    });
  }

  return (
    <div>
      <h2>Tabela: Dados de FOB por Vias</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Produto</th>
            <th>Quantidade de Operações</th>
            <th>Somatório do FOB (US$)</th>
            <th>Média do FOB (US$)</th>
            <th>Desvio padrão do FOB (US$)</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row: any, index: number) => (
            <tr key={index}>
              <td>{row[0]}</td>
              <td>{row[1]}</td>
              <td>{formattedPrice(row[2])}</td>
              <td>{formattedPrice(row[2] / 12)}</td>
              {data_desvio[index] ? (
                <td>{formattedPrice(data_desvio[index])}</td>
              ) : (
                <td>0</td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
