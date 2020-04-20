import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { getCourses } from '../../actions/courses'

import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'

export class CoursesChooser extends Component {
  static propTypes = {
    courses: PropTypes.array.isRequired,
    getCourses: PropTypes.func.isRequired,
  }

  componentDidMount() {
    this.props.getCourses()
  }

  render() {
    const courseOptions = () => {
      return this.props.courses.map((course) => (
        <option key={course.id} value={course.id}>
          {course.language} | {course.level}
        </option>
      ))
    }

    return (
      <div>
        <Form>
          <Form.Group controlId='exampleForm.ControlSelect1'>
            <Form.Row>
              <Form.Label column='lg' xs={4} md={2}>
                Courses
              </Form.Label>
              <Col xs={8} md={4}>
                <Form.Control as='select' size='lg'>
                  {courseOptions()}
                </Form.Control>
              </Col>
            </Form.Row>
          </Form.Group>
        </Form>
      </div>
    )
  }
}

const coursesSelector = (state) => state.coursesReducer.courses

const mapStateToProps = (state) => ({
  courses: coursesSelector(state),
})

export default connect(mapStateToProps, { getCourses })(CoursesChooser)
