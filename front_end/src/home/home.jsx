import React from 'react'
import { Link } from "react-router-dom";

import Button from '../components/button/button'
import Text from '../components/input/text'
import HomeService from './home.service'
import './home.css'

class Home extends React.Component {
  _service = new HomeService()

  constructor(props) {
    super(props);
    this.state = {
      date: new Date().toISOString().slice(0,10),
      subjects: []
    }
  }

  componentDidMount(){
    this._service.subject().then(
      subjects => this.setState({subjects})
    )
  }

  updateDate(event) {
    this.setState({ date: event.target.value })
  }

  render() {
    if(!this.state.subjects) {
      return (<h2 className="text-center">Não foi possível carregar os dados</h2>)
    }
    return (
      <div className="container-subjects">
        <div className="text-center">
          <b>Dia da aula</b>
        </div>

        <Text
          type="date"
          onChange={(event)=> this.updateDate(event)}
          defaultValue={new Date().toISOString().slice(0,10)}
        />

        <div className="text-center">
          {this.state.subjects.map((subject, key) => 
            <Link to={`attendances/${subject.id}/${this.state.date}`} key={key}>
              <Button type="primary rounded" text={subject.name} />
            </Link>
          )}
        </div>
      </div>
    )
  }
}
export default Home;