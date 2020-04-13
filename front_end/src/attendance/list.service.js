import axios from 'axios';

class ListService {
  students(subject, date) {
    return axios.get(
      `${process.env.REACT_APP_API}/attendances/${subject}/${date}`,
    ).then(all => all.data)
  }

  register(student, subject, attendance, date) {
    return axios.post(
      `${process.env.REACT_APP_API}/attendances/${subject}/${date}`, 
    { student, attendance })
    .then(result => 
      (result.status > 200 && result.status < 299) && result.data.msg === "success"
    ).catch(error => false)
  }

}

export default ListService;