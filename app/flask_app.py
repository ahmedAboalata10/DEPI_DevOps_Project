from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def show_project_info():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>DEPI DevOps Project</title>
    <style>
      html,
      body {
        margin: 0;
        padding: 0;
      }
      /* ========================== */
      .header {
        width: 100%;
        height: 100vh;
        background-image: url(/static/docker2.jpg);
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        overflow: hidden;
        position: relative;
      }

      .layer {
        width: 100%;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.7);
      }

      /* ========== Header-Section ================== */

      .header .content {
        text-align: center;
        padding: 1.25rem;
        margin: 0 auto;
      }

      .header .content h1 {
        font-size: 4rem;
        color: #fff;
        margin-top: 6rem;
      }

      .header .content .caption {
        margin: 23vh auto 0;
        padding-bottom: 0.3125rem;
      }
      .header .content .caption h2 {
        color: #f8f9fa;
      }

      /* ================ Team-Members-Section ================ */
      .container {
        width: 90%;
        margin: auto;
      }

      .members-name .container {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
      }
      .team-members {
        color: #f8f9fa;
        font-size: large;
        font-weight: 900;
      }

      .team-members p {
        color: #ffbd59;
        font-size: x-large;
      }

      .members-name {
        background-color: rgba(128, 128, 128, 0.3);
        width: 50%;
        height: 15.625rem;
        margin: auto;
      }
      ul {
        list-style-type: none;
        padding: 0;
      }
      li {
        transition: transform 0.2s ease;
        margin-bottom: 2.125rem;
        font-size: large;
        font-weight: 900;
      }

      .members-name .lists-left {
        margin-bottom: 0.3125rem;
        text-align: start;
      }

      .members-name .lists-right {
        margin-left: auto;
        margin-bottom: 0.3125rem;
        text-align: start;
      }

      li:hover {
        transform: scale(1.05);
        color: #ffd700;
      }

      /* ======================= */

      @media screen and (max-width: 770px) {
        .members-name {
          width: 100%;
          height: auto;
        }
      }
    </style>
    <!-- <link rel="stylesheet" href="css/main.css" /> -->
  </head>
  <body>
    <div class="header">
      <div class="layer">
        <div class="content">
          <h1>DEPI DevOps Project</h1>
          <div class="caption">
            <h2>Automated Deployment Pipeline with Jenkins and Docker</h2>

            <div class="team-members">
              <p>Team Members:</p>

              <div class="members-name">
                <div class="container">
                  <ul class="lists-left">
                    <li>Fatma Elzahraa Ali</li>
                    <li>Mohammed Yousry</li>
                    <li>Asmaa Tarek</li>
                  </ul>
                  <ul class="lists-right">
                    <li>Ahmed Abou Elata</li>
                    <li>Esraa Eissa</li>
                  
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

