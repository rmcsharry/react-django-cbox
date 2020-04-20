import React from 'react'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import styles from './styles.scss'
import DayJS from 'react-dayjs'

function SectionTitle({ title }) {
  const dayjs = require('dayjs')
  const today = dayjs().format('MMMM D, YYYY')

  return (
    <Row>
      <Col>
        <div className={`${styles.headerContainer} bg-light`}>
          {title.includes('student') ? (
            <div className='row no-gutters'>
              <h5 className='col'>Week of {today}</h5>
              <h5 className='float-right'>{title}</h5>
            </div>
          ) : (
            <h3>{title}</h3>
          )}
        </div>
      </Col>
    </Row>
  )
}

export default SectionTitle
