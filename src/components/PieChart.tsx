import { Chart } from "react-google-charts";

type Props = {
  dados: any;
};

export const PieChart = ({ dados }: Props) => {
  const data = [["Task", "Hours per Day"], ...dados];
  return (
    <div>
      <Chart
        chartType="PieChart"
        data={data}
        options={{
          title: "My Daily Activities",
        }}
        width={"100%"}
        height={"400px"}
      />
    </div>
  );
};

export default PieChart;
