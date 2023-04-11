import { Chart } from "react-google-charts";

type Props = {
  dados: any;
  title: string;
};

export const PieChart = ({ dados, title }: Props) => {
  const data = [["Produto", "FOB (US$)"], ...dados];
  return (
    <div>
      <Chart
        chartType="PieChart"
        data={data}
        options={{
          title,
        }}
        width={"100%"}
        height={"400px"}
      />
    </div>
  );
};

export default PieChart;
