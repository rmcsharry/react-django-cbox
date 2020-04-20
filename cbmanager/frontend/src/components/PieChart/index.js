import React from 'react'
import { ResponsivePie } from '@nivo/pie'
// make sure parent container have a defined height when using
// responsive component, otherwise height will be 0 and
// no chart will be rendered.

export default function PieChart({ data }) {
  return (
    <ResponsivePie
      data={data}
      margin={{ top: 40, right: 80, bottom: 80, left: 80 }}
      innerRadius={0.5}
      padAngle={0.7}
      cornerRadius={3}
      colors={{ scheme: 'pastel1' }}
      borderWidth={1}
      borderColor={{ theme: 'background' }}
      radialLabelsSkipAngle={10}
      radialLabelsTextXOffset={6}
      radialLabelsTextColor="#333333"
      radialLabelsLinkOffset={0}
      radialLabelsLinkDiagonalLength={16}
      radialLabelsLinkHorizontalLength={24}
      radialLabelsLinkStrokeWidth={1}
      radialLabelsLinkColor={{ from: 'color' }}
      slicesLabelsSkipAngle={10}
      slicesLabelsTextColor="#333333"
      animate={true}
      motionStiffness={90}
      motionDamping={15}
      defs={[
        {
          id: 'dots',
          type: 'patternDots',
          background: 'inherit',
          color: 'rgba(255, 255, 255, 0.3)',
          size: 4,
          padding: 1,
          stagger: true
        },
        {
          id: 'lines',
          type: 'patternLines',
          background: 'inherit',
          color: 'rgba(255, 255, 255, 0.3)',
          rotation: -45,
          lineWidth: 6,
          spacing: 10
        }
      ]}
      fill={[
        {
          match: {
            id: 'ontrack'
          },
          id: 'dots'
        },
        {
          match: {
            id: 'slow'
          },
          id: 'dots'
        },
        {
          match: {
            id: 'inactive'
          },
          id: 'lines'
        },
      ]}
      legends={[
        {
          anchor: 'bottom',
          direction: 'row',
          translateY: 80,
          itemWidth: 70,
          itemHeight: 18,
          itemTextColor: '#999',
          symbolSize: 16,
          symbolShape: 'square',
          effects: [
            {
              on: 'hover',
              style: {
                itemTextColor: '#000'
              }
            }
          ]
        }
      ]}
    />
  )
}
