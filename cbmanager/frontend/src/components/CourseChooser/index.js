import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { getCourses } from '../../actions/courses'

import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'

export class CoursesChooser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      selectedValue: 0,
    }
    this.handleChoice = this.handleChoice.bind(this)
  }

  static propTypes = {
    courses: PropTypes.array.isRequired,
    getCourses: PropTypes.func.isRequired,
    allOption: PropTypes.shape({
      label: PropTypes.string,
      value: PropTypes.number
    })
  }

  componentDidMount() {
    this.props.getCourses()
    this.setState({
      selectedValue: this.props.defaultValue,
    })
  }

  handleChoice(selectedOption) {
    this.setState({ selectedValue: selectedOption.target.value })
    console.log(selectedOption.target.value)
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
                <Form.Control
                  as='select'
                  size='lg'
                  value={
                    this.props.courses.filter(
                      ({ id }) => id === this.state.selectedValue
                    ).id
                  }
                  onChange={this.handleChoice}
                >
                  <option value={this.props.allOption.value}>{this.props.allOption.label}</option>
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
  allOption: {
    label: "All courses",
    value: 0
  }
})

export default connect(mapStateToProps, { getCourses })(CoursesChooser)
