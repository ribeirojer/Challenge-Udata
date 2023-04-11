import React from "react";

type Props = {
  data: any;
  data_correlacao: any;
};

const Table = ({ data, data_correlacao }: Props) => {
  return (
    <div>
      {JSON.stringify(data_correlacao)}
      <table className="table">
        <thead>
          <tr>
            <th>Produto</th>
            <th>Quantidade de Vezes</th>
            <th>Somatório do FOB</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row: any, index: number) => (
            <tr key={index}>
              <td>{row[0]}</td>
              <td>{row[1]}</td>
              <td>{row[2]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
