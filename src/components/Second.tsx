import { Chart } from "react-google-charts";

type Props = {
  dados: any;
};

export const Second = ({ dados }: Props) => {
  const options = {
    title: "Vias por mês",
    vAxis: { title: "FOB (US$)" },
    hAxis: { title: "Mês" },
    seriesType: "bars",
    series: { 6: { type: "line" } },
    colors: ['#72148C', '#B86AD9', '#692CBF','#72148C', '#B86AD9', '#692CBF', '#8C5642', '#F2F2F2']

  };
  return (
    <div>
      <Chart
        chartType="ComboChart"
        width="100%"
        height="400px"
        data={dados}
        options={options}
      />
    </div>
  );
};

export default Second;
