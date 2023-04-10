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
