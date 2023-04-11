import { Chart } from "react-google-charts";

type Props = {
  data: any;
};

const MapChart = ({ data }: Props) => {
  return (
    <div>
      <Chart
        chartEvents={[
          {
            eventName: "select",
            callback: ({ chartWrapper }) => {
              const chart = chartWrapper.getChart();
              const selection = chart.getSelection();
              if (selection.length === 0) return;
              const region = data[selection[0].row + 1];
              console.log("Selected : " + region);
            },
          },
        ]}
        chartType="GeoChart"
        width="100%"
        height="400px"
        data={data}
        options={{
          colors: ["#B86AD9", "#72148C", "#72148C", "#8C5642"],
        }}
      />
      <h2>Mapa de importações</h2>
    </div>
  );
};

export default MapChart;
