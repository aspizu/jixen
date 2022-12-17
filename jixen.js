/**
 * @param {number} timestamp
 * @returns {Date}
 */
export function dateFromEpoch(timestamp) {
  const d = new Date(0)
  d.setUTCSeconds(timestamp)
  return d
}

/**
 * @param {string} url
 */
export async function get(url) {
  return await (await fetch(url)).json()
}

/**
 * @param {string} url
 * @param {object} json
 */
export async function post(url, json) {
  return await (
    await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(json),
    })
  ).json()
}

/**
 * @param {Date} date
 * @param {string} format
 * @returns {string}
 */
export function strftime(date, format) {
  let out = ''
  for (let i = 0; i < format.length; i++) {
    if (format[i] == '%') {
      i += 1
      const c = format[i]
      if (c == '%') {
        out += '%'
      } else if (c == 'a') {
        out += ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][date.getDay()]
      } else if (c == 'A') {
        out += [
          'Monday',
          'Tuesday',
          'Wednesday',
          'Thursday',
          'Friday',
          'Saturday',
          'Sunday',
        ][date.getDay()]
      } else if (c == 'b') {
        out += [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec',
        ][date.getMonth()]
      } else if (c == 'd') {
        out += String(date.getDate()).padStart(2, '0')
      } else if (c == 'e') {
        out += String(date.getDate()).padStart(2, ' ')
      } else if (c == 'H') {
        out += String(date.getHours()).padStart(2, '0')
      } else if (c == 'I') {
        out += String(1 + ((date.getHours() - 1) % 12)).padStart(2, '0')
      } else if (c == 'k') {
        out += String(date.getHours()).padStart(2, ' ')
      } else if (c == 'l') {
        out += String(1 + ((date.getHours() - 1) % 12)).padStart(2, ' ')
      } else if (c == 'm') {
        out += String(date.getMonth()).padStart(2, '0')
      } else if (c == 'M') {
        out += String(date.getMinutes()).padStart(2, '0')
      } else if (c == 'p') {
        if (date.getHours < 12) {
          out += 'AM'
        } else {
          out += 'PM'
        }
      } else if (c == 'P') {
        if (date.getHours < 12) {
          out += 'am'
        } else {
          out += 'pm'
        }
      } else if (c == 'S') {
        out += date.getUTCSeconds()
      } else if (c == 'u') {
        out += date.getDay()
      } else if (c == 'w') {
        out += date.getDay() - 1
      } else if (c == 'y') {
        out += String(date.getFullYear() % 100).padStart(2, '0')
      } else if (c == 'Y') {
        out += String(date.getFullYear() % 10000).padStart(4, '0')
      }
    } else {
      out += format[i]
    }
  }
  return out
}
