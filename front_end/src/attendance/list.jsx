import React from 'react';

import './list.css'
import ListService from './list.service.js';
import Input from '../components/input/text';
import Alert from '../components/alert/alert';
import { STATUS_ATTENDANCES } from '../constants'
import Checkbox from '../components/input/checkbox';

class List extends React.Component {
  _date = this.props.match.params.date
  _service = new ListService();
  _setTimeoutUpdate;
  _setTimeoutAlert;

  constructor(props) {
    super(props);
    this.state = {
      data: []
    }
  }

  componentDidMount() {
    this.loadList();
  }

  loadList() {
    const {date, id} = this.props.match.params;
    this._service.students(id, date).then(value => {
      value = value.length > 0 ? value : [{empty: "Sem alunos cadastrados"}];
      this.setState({data: value })
    }).catch(error => {
      this.setState({data: [{error: "Erro durante a recuperação dos dados!"}]})
    });
  }

  refreshList() {
    clearTimeout(this._setTimeoutUpdate);
    this._setTimeoutUpdate = setTimeout(() => this.loadList(), 500)
  }

  register(event, student, subject) {
    if ( !event?.target || !student || !subject ) {
      return false;
    }
    const target = event.target;
    const isAttendance = target.checked;
    const {date} = this.props.match.params;

    this._service.register(
      student, subject, isAttendance, date
    ).then(result => {
      if(!result) {
        target.checked = false;
      }

      result ? this.boxAlert('success', 'Salvo com sucesso!') : 
        this.boxAlert('danger', 'Erro ao salvar!')

      if(result) {
        this.refreshList()
      }
    }).catch(error => this.loadList());
  }

  boxAlert(type, text) {
    clearTimeout(this.setTimeoutAlert)
    this.setState({
      alert: { type, text }
    })
    
    this.setTimeoutAlert = setTimeout(() => this.setState({ alert: {} }), 1000)
  }

  search(event) {
    const text = (event.target.value || '').trim();

    if(this.state.initial_data === undefined) {
      this.setState({initial_data: this.state.data});
    }
    let data = this.state.initial_data || this.state.data;

    if(text.length === 0 ) {
      return this.setState({data});
    }

    data = data.filter(
      value => value.student.name.toLowerCase().indexOf(text.toLowerCase()) >= 0
    );

    this.setState({data});
  }

  render() {
    return (
      <div className="container">
        <Alert text={this.state.alert?.text} type={this.state.alert?.type} />
        <div className="search">
          <p>
            <b>Buscar</b>
          </p>
          <Input
            onChange={(event) => this.search(event)}
            name=""
            defaultValue=""
            placeholder="Digite o nome do aluno"
          />
        </div>

        <div className="container-list">
          <p className="title text-center">
            <b>Alunos da lista de presença - {this._date.split('-').reverse().join('-')}</b>
          </p>

          <div>
            <ol className="list">
              {this.state.data.map( (key, value) => this.newLine(key, value))}
            </ol>
          </div>

        </div>
      </div>
    )
  }

  newLine(value, key) {
    if (value.empty) {
      return <div className="text-center" key={key}>{value.empty}</div>
    }
    if (value.error) {
      return <div className="text-center" key={key}>{value.error}</div>
    }

    let name = value.student?.name;
    if(name) {
      name = value.attendance?.id ? name : `${name} - Pendente`
    }

    const checked = value.attendance?.status_id === STATUS_ATTENDANCES['PRESENTE']

    return (
      <li key={key}>
        <Checkbox
          type="checkbox"
          defaultChecked={ checked }
          label={ name || "Erro ao recuperar aluno" }
          onClick={ (event)=> this.register(
            event, value.student?.id, value.subject?.id
          )}
        />
      </li>
    );
  }
}

export default List;
