import { Chart } from "react-google-charts";

type Props = {
  title: string;
  namedata: string;
  dados: any;
};

const First = ({ title, namedata, dados }: Props) => {
  const data = [[namedata, "FOB (US$)"], ...dados];
  const options = {
    chart: {
      title: title,
    },
    colors: ['#72148C', '#B86AD9', '#692CBF', '#8C5642', '#F2F2F2']
  };
  return (
    <div>
      <Chart
        chartType="Bar"
        width="100%"
        height="400px"
        data={data}
        options={options}
      />
    </div>
  );
};

export default First;
